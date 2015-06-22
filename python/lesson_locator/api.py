#!/usr/bin/env python
"""
api.py

The API for the Felden Lesson Locator site.

Copyright (c) 2015 Mind In Motion
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import datetime
import json
import os
import re
import string

import pyramid.renderers
import pyramid.view

import const

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
# API Methods
# ---------------------------------------------------------------------------------------------
@pyramid.view.view_config(route_name='api.lessons', renderer='json')
def getLessons(request):
    """
    Get the full list of Feldenkrais Lessons that are available.
    """
    print("Getting the full list of lessons...")

    lessons = list()

    data_dir = getDataDir()

    for lesson_file in sorted(os.listdir(data_dir)):
        if re.search(r'^\.', lesson_file):
            continue

        lesson_path = os.path.join(data_dir, lesson_file)
        fh = open(lesson_path)
        lesson_json = json.load(fh)
        fh.close()

        tmp_lesson = dict()
        tmp_lesson['title'] = lesson_json['description']
        tmp_lesson['number'] = lesson_json['number']
        tmp_lesson['id'] = re.sub(r'\.json$', '', lesson_file)

        lessons.append(tmp_lesson)

    return lessons


@pyramid.view.view_config(route_name='api.lesson', renderer='json')
def getLesson(request):
    """
    Get the JSON representation for a lesson.
    """
    print("getLesson called...")

    lesson_id = None
    if 'lesson_id' in request.matchdict:
        lesson_id = request.matchdict['lesson_id']

    if lesson_id is None:
        # This should return an appropriate error about not finding the
        # requested lesson.
        pass

    lesson = getLessonById(lesson_id)
    return lesson


def getLessonById(lesson_id):
    """
    Get the data structure that represents the lesson. It will be read from
    disk and some processing will then get run on the lesson.
    """
    print("Getting lesson '%s'..." % lesson_id)

    data_dir = getDataDir()

    lesson_path = os.path.join(data_dir, lesson_id + ".json")
    fh = open(lesson_path)
    raw_lesson = json.load(fh)
    fh.close()

    lesson = dict()
    lesson['description'] = raw_lesson['description']
    lesson['number'] = raw_lesson['number']

    if 'annotations' in raw_lesson:
        lesson['annotations'] = dict()
        for item in raw_lesson['annotations']:
            new_item = re.sub(r'-', '_', item)
            lesson['annotations'][new_item] = raw_lesson['annotations'][item]

    else:
        lesson['annotations'] = dict()
        lesson['annotations']['name'] = "There are no lesson annotations for this lesson"

    for item in lesson['annotations']:
        if re.search(r'-', item):
            item = re.sub(r'-', '_', item)

    for item in lesson['annotations']:
        print(item)

    # Get the sections of the lesson.
    if 'sections' in raw_lesson:
        lesson['sections'] = raw_lesson['sections']
    else: 
        # The lesson had no sections. Run through the lesson section
        # starts and compute the various sections for the lesson.
        lesson['sections'] = list()

        previous_section_start = None
        for next_section_start in raw_lesson['parsed']['section_starts']:

            if previous_section_start is None:
                previous_section_start = next_section_start
                continue

            # Get the lines starting from previous_section_start to just before the
            # next_section_start.
            section = dict()
            section['label'] = ""
            section['text'] = list()

            for line in raw_lesson['text'][previous_section_start:next_section_start]:
                if re.search(r'^\s*$', line): continue
                section['text'].append(line)

            if len(section['text']):
                mobj = re.search(r'^(\d+\w?)\.\s*', section['text'][0])
                if mobj:
                    section['label'] = mobj.group(1)
                    section['text'][0] = re.sub(r'^\d+\w?\.\s*', "", section['text'][0])

            lesson['sections'].append(section)

            previous_section_start = next_section_start

    return lesson


def getDataDir():
    """ Get the appropriate data directory.
    """
    if const.LESSON_LOCATOR_ROOT is None:
        msg = "Required value, const.LESSON_LOCATOR_ROOT, is not available"
        raise LessonLocatorAPIError(msg)

    data_dir = os.path.join(const.LESSON_LOCATOR_ROOT, "data/alexander_yanai/annotated")
    return data_dir

#    data_dir_dev = "/Users/kcureton/Documents/work/felden/data/alexander_yanai/annotated"
#    if os.path.exists(data_dir_dev):
#        return data_dir_dev
#
#    data_dir_prod = "/var/www/code/felden/data/alexander_yanai/annotated"
#    if os.path.exists(data_dir_prod):
#        return data_dir_prod


class LessonLocatorAPIError(Exception):
    pass


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is the test harness for the module")
    sys.exit(0)

# lesson_locator
The Feldenkrais Lesson Locator web application

Overview
======================
The Lesson Locator allows Feldenkrais practitioners to quickly search for lessons.
The goal is to build a system that provides a search interfaces that is geared towards
Feldenkrais and the kinds of searches someone might do in practice.



Code Organization
======================
The source code is layout out as follows:

    bin/
        Command line tools for parsing text-based lesson data, adding annotations to
        exiting lessons, and other maintenance tasks.

    data/
        Where the lesson data lives. This requires you have access to the lessons in text
        form. They are copyrighted, so they are not included here.

    devops/
        The Ansible setup for creating a virtual machine and install the lesson locater
        web application, including configing the OS web server properly.

    etc/
        Any configuration files needed by the lesson locator.

    python/
        Python modules used by the lesson locator bin tools and site scripts.

    site/
        The WSGI scripts live here. The felden.dev.wsgi script is intended for running on
        the command-line (used by developers for quick dev iteration).

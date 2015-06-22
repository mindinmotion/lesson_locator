/*
 * app.js
 */

var lessonLocatorApp = angular.module('lessonLocatorApp', [
    'ui.router',
    'lessonLocatorApp.controllers',
    'lessonLocatorApp.lessons'
]);


lessonLocatorApp.config(['$interpolateProvider',
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
    }
]);


lessonLocatorApp.config(['$stateProvider', '$urlRouterProvider',
    function($stateProvider, $urlRouterProvider) {
        $stateProvider
            .state("lessons", {
                abstract: true,
                url: "/lessons",
                templateUrl: "/snipets/lessons.html",
                resolve: {
                    lessons: ['lessonsFactory', function(lessonsFactory){
                        return lessonsFactory.list();
                    }]
                }
            })
            .state("lessons.list", {
                url: "",
                templateUrl: "/snipets/lessons.list.html",
                controller: "LessonsListController"
            })
            .state("lessons.detail", {
                url: "/lessons/{lessonId:ay_[0-9][0-9][0-9][0-9]}",
                templateUrl: "/snipets/lesson.detail.html",
                controller: "LessonDetailController"
            });

        $urlRouterProvider.otherwise("/lessons");
    }
]);

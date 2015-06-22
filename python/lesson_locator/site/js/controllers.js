/*
 * controllers.js
 */

angular.module('lessonLocatorApp.controllers', [
])

.controller('LessonsController', ['$scope', '$stateParams', 'lessonsFactory',
    function($scope, $stateParams, lessonsFactory) {
        $scope.lessons = [];
    }
])

.controller('LessonsListController', ['$scope', '$http',
    function($scope, $http) {
        /*$scope.lessons = lessonsFactory.list();*/
        var url = "/api/lessons"
        $http.get(url)
            .success(function(data) {
                $scope.lessons = data;
            })
            .error(function() {
                $scope.lessons = [];
            });
    }
])

.controller('LessonDetailController', ['$scope', '$stateParams', '$http',
    function($scope, $stateParams, $http) {
        /*$scope.lesson = lessonsFactory.get($stateParams.lessonId);*/
        var url = "/api/lesson/" + $stateParams.lessonId;
        var my_lesson = $http.get(url)
            .success(function(data) {
                $scope.lesson = data;
            })
            .error(function() {
                $scope.lessons = {};
            });
    }
]);

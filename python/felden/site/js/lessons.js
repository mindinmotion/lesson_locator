/*
 * lessons.js
 */

angular.module('lessonLocatorApp.lessons', [
    'ngResource'
])

.factory('lessonsFactory', ['$http',

    /*
    function($resource) {
        return $resource("/api/lessons", {}, {}
    }
    */

    function($http) {
        var factory = {};
        factory.list = function() {
            var url = "/api/lessons"
            var my_lessons = $http.get(url)
                .success(function(data) {
/*                    alert("Got the list of lessons");
*/
                    return data;
                })
                .error(function() {
                    alert("Failed to get the list of lessons");
                    return null;
                });
    
            /*
            var my_lessons = [
                { 'id': "ay_0001", 'title': 'Lesson #0001' },
                { 'id': "ay_0002", 'title': 'Lesson #0002' },
                { 'id': "ay_0003", 'title': 'Lesson #0003' },
                { 'id': "ay_0004", 'title': 'Lesson #0004' }
            ];
            */

            return my_lessons;
        };

        factory.get = function(id) {
            var url = "/api/lesson/" + id
            var my_lesson = $http.get(url)
                .success(function(data) {
/*                    alert("SUCCESS: getting lesson " + id);
*/
                    return data;
                    /*
                    my_lesson = {
                        'text': [
                            'Bogus lesson.',
                            'Bogus lesson.',
                            'Bogus lesson.',
                            'Bogus lesson.',
                            'Bogus lesson.'
                        ],
                        'description': "This is a lesson " + id,
                        'number': "1"
                    };
                    */
                })
                .error(function() {
                    alert("FAILURE: getting lesson " + id);
                    return null;
                });
        };

        return factory;
    }
]);

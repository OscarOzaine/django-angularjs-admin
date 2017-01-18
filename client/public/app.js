'use strict';

var retail = angular.module("retail", ['ngCookies']);

angular.module('SampleApplication', [
    'appRoutes',
    'retail',
    'ngResource'
])
.run(function($cookieStore, $rootScope, $http) {
  	if ($cookieStore.get('djangotoken')) {
		$http.defaults.headers.common['Authorization'] = 'Token ' + $cookieStore.get('djangotoken');
		//document.getElementById("main").style.display = "block";
    } else {
    	//document.getElementById("id_auth_form").style.display = "block";
    }
})
;
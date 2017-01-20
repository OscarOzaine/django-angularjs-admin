'use strict';

var retail = angular.module("retail", ['ngCookies']);

angular.module('SampleApplication', [
    'appRoutes',
    'retail',
    'ngResource',
    'base64',
])
.run(function($cookieStore, $rootScope, $http, $base64) {
	/*
	console.log('run');
	var auth = $base64.encode('oz:oz');
	console.log(auth);
    var headers = {"Authorization": "Basic " + auth};
	$http.defaults.headers.common['Authorization'] = 'Token ' + auth;
	$http.defaults.useXDomain = true;
  	if ($cookieStore.get('djangotoken')) {
  		//var auth = $base64.encode($scope.username + ":" + $scope.password);
  		var auth = $base64.encode('oz:oz');
  		console.log(auth);
        var headers = {"Authorization": "Basic " + auth};
		$http.defaults.headers.common['Authorization'] = 'Token ' + auth;
		//document.getElementById("main").style.display = "block";
    } else {
    	//document.getElementById("id_auth_form").style.display = "block";
    }
    */
})
;
angular.module('appRoutes', ["ui.router"])
	.config([
		'$stateProvider', 
		'$urlRouterProvider', 
		'$qProvider', 
		function($stateProvider, $urlRouterProvider, $qProvider) {
			$qProvider.errorOnUnhandledRejections(false);
		    $stateProvider
			    .state({
			        name: 'internal',
			        url: '/internal',
			        templateUrl: 'public/components/internal/templates/internal.template.html',
			        controller: 'InternalController'
			    })
			    .state({
			        name: 'sensors',
			        url: '/sensors',
			        templateUrl: 'public/components/internal/templates/sensors.template.html',
			        controller: 'SensorController'
			    })
			    .state({
			        name: 'sensors_view',
			        url: '/sensors/:id',
			        templateUrl: 'public/components/internal/templates/sensors/view.html',
			        controller: 'SensorViewController'
			    })
			    .state({
			        name: 'login',
			        url: '/login',
			        templateUrl: 'public/components/internal/templates/login.template.html',
			        controller: 'LoginController'
			    })
			    ;

		    $urlRouterProvider.otherwise('/login');
		}
]);
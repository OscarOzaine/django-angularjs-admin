angular.module('appRoutes', ["ui.router"])
	.config([
		'$stateProvider', 
		'$urlRouterProvider', 
		function($stateProvider, $urlRouterProvider) {

		    $stateProvider
		    	.state({
			        name: 'retail',
			        url: '/',
			        templateUrl: 'public/components/retail/templates/retail.template.html',
			        controller: 'RetailController'
			    })
			    .state({
			        name: 'login',
			        url: '/login',
			        templateUrl: 'public/components/retail/templates/login.template.html',
			        controller: 'LoginController'
			    })
			    ;

		    $urlRouterProvider.otherwise('/');
		}
]);
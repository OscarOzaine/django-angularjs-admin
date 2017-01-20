retail.controller('LoginController', function($scope, Session, $base64, Chain, api, $http, $cookieStore) {
    
    $scope.getCredentials = function() {
        return {username: $scope.username, password: $scope.password};
    };

    $scope.login = function() {
        console.log('login');
        var credentials = $scope.getCredentials();
        //var auth = $base64.encode($scope.username + ":" + $scope.password);
        //var headers = {"Authorization": "Basic " + auth};
        console.log(credentials);
        console.log(Session.getUser());
        api.login(credentials, Session.getUser());
    };
});
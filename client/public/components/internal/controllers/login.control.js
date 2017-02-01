retail.controller('LoginController', function($scope, Session, $location, $base64, Chain, api, $http, $cookieStore) {
    
    if (Session.isAuthenticated()) {
        console.log('redirect');
        $location.path('internal').replace();
    }

    $scope.getCredentials = function() {
        return {username: $scope.username, password: $scope.password};
    };

    $scope.login = function() {
        console.log('login');
        var credentials = $scope.getCredentials();
        //var auth = $base64.encode($scope.username + ":" + $scope.password);
        //var headers = {"Authorization": "Basic " + auth};
        //console.log(credentials);
        //console.log(Session.getUser());
        var access = api.login(credentials, Session.getUser()).then(
           function(response) {
                //console.log('response');
                //console.log(response);
                if (response.data != "-1") {
                    
                    Session.saveUser(response.data.username);
                    Session.saveAuthToken($base64.encode($scope.username + ":" + $scope.password));
                    //authState.user = (response.data.username);
                    console.log('access granted');
                    $location.path('internal').replace();
                } else {
                    console.log("access not granted");
                }
                //console.log(response.data); 
           }
        ).catch(function (data) {
            //console.log('error data');
            //console.log(data.status);

            if (data.status == 403) {
                window.location.reload();
                $location.path('login').replace();
            }
            //console.log(data);
            // Handle error here
        });
        //console.log('access');
        //console.log(access);
    };

});
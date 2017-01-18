retail.controller('LoginController', function($scope, Chain, Store, Employee, $http, $cookieStore) {
    $scope.login = function() {
        console.log('login');
        var user_data = {
            "username": $scope.username,
            "password": $scope.password
        };
         
        //$http.post(constants.serverAddress + "api-token-auth", user_data)
        $http.post("http://localhost:8000/api-auth/", user_data)
            .then(function(response) {
                //$cookieStore.put('djangotoken', response.token);
                var token = Base64.encode('username' + $scope.username + ':' + $scope.password + 'password');
                $http.defaults.headers.common['Authorization'] = 'Token ' + token;
                console.log(token);
                authService.loginConfirmed();
            }
        );
        /*
        console.log($scope.username);
        console.log($scope);
        */
        /*
        var credentials = $scope.getCredentials();
        console.log(credentials);
        
        $http.post('/api/auth\\', credentials, {"Authorization": ('Basic ' + btoa(credentials.username + ':' + credentials.password))})
            .success(function(response) {
                //$cookieStore.put('djangotoken', response.token);
                $http.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded';
                $http.defaults.headers.common['Authorization'] = ('Basic ' + btoa(data.username + ':' + data.password));
                //$http.defaults.headers.common['Authorization'] = 'Token ' + response.token;
                //authService.loginConfirmed();
            });
        */
        /*
        api.auth.login(credentials).
            $promise.
                then(function(data){
                    authState.user = data.username;
                }).
                catch(function(data){
                    alert(data.data.detail);
                });
        */
        
        /*
        api.auth.login(credentials).$promise.
            then(function(data) {
                console.log('login');
                console.log(data);
                authState.user = data.username;
            }).
            catch(function(data) {
                console.log('catch');
                console.log(data);
                alert(data.data.detail);
            });
        */
    };
});
retail.factory('Session', function($cookies, $http) {
  var Session = {
    saveUser: function(user) { 
        $cookies.put('user', user);
    },
    getUser: function() { 
      return $cookies.get('user');
    },
    saveAuthToken: function(auth_token) {
        $http.defaults.headers.post['Authorization'] = 'Basic ' + auth_token;
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
        $cookies.put('auth_token', auth_token);
    },
    getAuthToken: function() { 
        return $cookies.get('auth_token');
    },
    deleteSession: function() {
        var cookies = $cookies.getAll();
        angular.forEach(cookies, function (v, k) {
            $cookies.remove(k);
        });
        $http.defaults.headers.post['Authorization'] = '';
    },
    isAuthenticated: function() {
        console.log('userrrrrrr='+$cookies.get('user'));
        if ($cookies.get('user') !== undefined) {
            return true;
        }

        return false;
    }
  };
  Session.getUser();
  return Session; 
});

retail.factory('api', function($resource, $base64, $http, $location, Session) 
{
    return {
        login: function(credentials, authLogin) {
            var auth = $base64.encode(credentials.username + ":" + credentials.password)
            //var auth = {username: credentials.username, password: credentials.password};
            Session.saveAuthToken(auth);
            $http.defaults.headers.common['Authorization'] = 'Basic ' + auth;
            var valid = 0;
            /*console.log(credentials);
            console.log(auth);*/
            console.log(auth);
            return $http.post('http://127.0.0.1:8000/login\\', 'username='+credentials.username+'&password='+credentials.password)
            ;

            /*$http.get('http://127.0.0.1:8000/snippets\\')
                .success(function(response) {
                    //$http.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded';
                    //$http.defaults.headers.common['Authorization'] = ('Basic ' + btoa(data.username + ':' + data.password));
                    console.log(response);
                });*/
            //console.log(credentials);
            //return credentials;
        } 
    };
});
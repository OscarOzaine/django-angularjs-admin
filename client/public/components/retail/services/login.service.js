retail.factory('Session', function($cookies) {
  var Session = {
    saveUser: function(user) { 
        $cookies.put('user', user);
    },
    getUser: function() { 
      return $cookies.get('user');
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
            //$http.defaults.headers.common['Authorization'] = 'Basic ' + auth;
            var valid = 0;
            console.log(credentials);
            console.log(auth);
            $http.defaults.headers.post['Authorization'] = 'Basic ' + auth;
            $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
            $http.post('http://127.0.0.1:8000/login\\', 'username='+credentials.username+'&password='+credentials.password)
            .then(
               function(response) {
                    
                    if (response.data != "-1") {
                        Session.saveUser(response.data.username);
                        //authState.user = (response.data.username);
                        console.log('authState=' + Session.getUser());
                        console.log(Session.getUser());
                        $location.path('internal');
                    } else {
                        console.log("Not");
                    }
                    console.log(response.data); 
               }
            );

            /*$http.get('http://127.0.0.1:8000/snippets\\')
                .success(function(response) {
                    //$http.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded';
                    //$http.defaults.headers.common['Authorization'] = ('Basic ' + btoa(data.username + ':' + data.password));
                    console.log(response);
                });*/
            console.log(credentials);
            return credentials;
        } 
    };
});
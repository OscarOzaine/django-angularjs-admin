retail.factory('RangeParameter', function($resource) {
    return $resource(
        'http://localhost:8000/range-parameter/',
        {},
        {
            'query': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type':'application/json',
                    'Access-Control-Allow-Origin': 'http://127.0.0.1:8081',
                }
            }
        },
        {
            stripTrailingSlashes: false
        }
    );
});
retail.factory('RangeParameter', function($http, Session) {
  var RangeParameter = {
    saveUser: function(user) { 
        //$cookies.put('user', user);
    },
    getRangeParameters: function() { 

        $http.defaults.headers.common['Authorization'] = 'Basic ' + Session.getAuthToken();
        return $http.get('http://127.0.0.1:8000/range-parameter\\');
    },
    deleteSession: function() {
        //var cookies = $cookies.getAll();
        //angular.forEach(cookies, function (v, k) {
        //    $cookies.remove(k);
        //});
    },
    isAuthenticated: function() {
        //console.log('userrrrrrr='+$cookies.get('user'));
        //if ($cookies.get('user') !== undefined) {
            //return true;
        //}

        //return false;
    }
  };
  RangeParameter.getRangeParameters();
  return RangeParameter; 
});
retail.factory('Login', function($resource) {
    return $resource(
        'http://localhost:8000/users/login/',
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
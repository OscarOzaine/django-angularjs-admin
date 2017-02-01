retail.controller('SensorController', function($scope, RangeParameter, Session, $location, Chain, Store, Employee) {
    
    console.log('test');
    console.log(Session.getUser());

    $scope.user = Session.getUser();

    if (!Session.isAuthenticated()) {
        console.log('redirect');
        $location.path('login').replace();
    }

    var sensors = RangeParameter.getRangeParameters().then(
       function(response) {
            console.log('response');
            console.log(response);

            if (response.data != "-1") {
                
                console.log('access granted');
                $scope.sensors = response.data;
            } else {
                console.log("access not granted");
            }
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
    console.log('sensors');
    console.log(sensors);

    $scope.delete = function(data) {
        console.log('delete');
        console.log(data);
    }

    $scope.logout = function() {
        console.log('logout');
        Session.deleteSession()
        $location.path('login').replace();
    };

});
//
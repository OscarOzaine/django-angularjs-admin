retail.controller('InternalController', function($scope, Session, Chain, Store, Employee) {
    console.log('test');
    console.log(Session.getUser());
    $scope.user = Session.getUser();
});
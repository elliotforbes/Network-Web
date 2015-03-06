var app = angular.module("myApp", []);

app.controller("raspberryController", function($scope, $http, $timeout){
    var poll = function() {
        $timeout(function() {
                $http.get("../../results/connectedPis.php")
                .success(function(response) {$scope.pis = response;})
                .error(function(data, status, header, config) {
                    console.log(alert, status, header, config);
                });
            poll();
        }, 1000);
    }
    poll();
});

//function throughputController($scope, $http, $timeout){
//
//    var poll = function(){
//        $timeout(function() {
//             $http.get("results/throughput.php")
//            .success(function(response) {$scope.throughput = response;})
//            .error(function(data,status, header, config) {
//               console.log(alert,status,header,config); 
//            }); 
//        });
//    }
//    poll();
//
//}
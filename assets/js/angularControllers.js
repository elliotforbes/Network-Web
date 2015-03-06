var app = angular.module("myApp", []);

app.filter('getById', function() {
  return function(input, id) {
    var i=0, len=input.length;
    for (; i<len; i++) {
      if (+input[i].id == +id) {
        return input[i];
      }
    }
    return null;
  }
});

app.controller("raspberryController", function($scope, $http, $timeout){
    var poll = function() {
        $timeout(function() {
                $http.get("results/connectedPis.php")
                .success(function(response) {$scope.pis = response;})
                .error(function(data, status, header, config) {
                    console.log(alert, status, header, config);
                });
            
                console.log($scope.pis);
            poll();
        }, 1000);
    }
    poll();
});


app.controller("throughputController", function($scope, $http, $timeout){
   var poll = function(){
        $timeout(function(){
            $http.get("results/throughtput.php")
            .success(function(response) {$scope.throughput = response;})
            .error(function(data, status, header, config){
                    console.log(alert, status, header,config); 
            });
            
            console.log($scope.throughput);
            
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

//
// function raspberryController($scope, $http, $timeout) {
//    var poll = function() {
//        $timeout(function() {
//                $http.get("results/connectedPis.php")
//                .success(function(response) {$scope.pis = response;})
//                .error(function(data, status, header, config) {
//                    console.log(alert, status, header, config);
//                });
//            poll();
//        }, 1000);
//    }
//    poll();
//}
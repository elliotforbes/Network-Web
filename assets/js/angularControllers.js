var app = angular.module("myApp", []);

//app.filter('getById', function() {
//  return function(input, id) {
//    var i=0, len=input.length;
//    for (; i<len; i++) {
//      if (+input[i].id == +id) {
//        return input[i];
//      }
//    }
//    return null;
//  }
//});
//
//app.controller('GraphCtrl', function($scope, $http, $timeout){
//    $scope.chart = null;
//    $scope.config = {};
//    $scope.config.data1 = "30,40,50,60,70,80";
//    $scope.config.data2 = "60,50,40,30,20,10";
//    
//    $scope.typeOptions=["line", "bar", "spline"];
//    
//    $scope.config.type1 = $scope.typeOptions[0];
//    $scope.config.type2 = $scope.typeOptions[1];
//    
//    var config = {};
//    config.bindto = '#testChart';
//    config.data = {};
//    config.data.json = {};
//    config.data.json.data1 = $scope.config.data1.split(",");
//    config.data.json.data2 = $scope.config.data2.split(",");    
//    config.axis = {"y":{"label":{"text":"Number of items", "position":"outer-middle"}}};
//    config.data.types={"data1":$scope.config.type1, "data2":$scope.config.type2};
//    var counter = 70;
//    $scope.chart = c3.generate(config);
//    
//    var poll = function() {
//        $timeout(function(){
//            $scope.config.data1.concat(",");
//            $scope.config.data1.concat(counter);
//            $scope.chart.load();
//            counter += 10;
//        }, 1000);
//    }
//    poll();
//    
//});

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

//app.controller("raspberryController", function($scope, $http, $timeout){
//    var poll = function() {
//        $timeout(function() {
//                $http.get("results/latency.php")
//                .success(function(response) {$scope.latency = response;})
//                .error(function(data, status, header, config) {
//                    console.log(alert, status, header, config);
//                });
//            
//                console.log($scope.latency);
//            poll();
//        }, 1000);
//    }
//    poll();
//});
//
//
//app.controller("throughputController", function($scope, $http, $timeout){
//   var poll = function(){
//        $timeout(function(){
//            $http.get("results/throughtput.php")
//            .success(function(response) {$scope.throughput = response;})
//            .error(function(data, status, header, config){
//                    console.log(alert, status, header,config); 
//            });
//            
//            console.log($scope.throughput);
//            
//        }, 1000);
//   }
//   poll();
//});

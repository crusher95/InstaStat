var app = angular.module('myApp', []);

var url = "http://localhost:5000/";
var user_details = "dashboard/user_details";
var non_followers = "dashboard/non_followers";
var followers = "dashboard/fans";

app.controller("UserProfile", function($scope, $http) {
  $scope.loading = true;

    $http.get(url+user_details)
    .success(function(response) {
      $scope.user_detail = response;
               $scope.loading = false;

    })
    .error(function(response) {
      $scope.loading = false;
          $scope.error = "Error fetching data";
    });
});

app.controller('NonFollowerCtrl', function($scope, $http) {

    $scope.loading = true;
    $scope.length = 0;

  $http.get(url+non_followers)
  .success(function (response) {
          $scope.length = response.length;

          $scope.nonFollowers = response;
           $scope.unfollow_button = "Unfollow";
       $scope.loading = false;


      })
  .error(function(response) {
      $scope.loading = false;
          $scope.error = "Error fetching data";
    });

        $scope.reload = function() {
                          $scope.length = 0;


            $scope.nonFollowers = [];

     $scope.loading = true;
  $http.get(url+non_followers)
  .success(function (response) {
          $scope.length = response.length;
          $scope.nonFollowers = response;

       $scope.loading = false;})
  .error(function(response) {
      $scope.loading = false;
          $scope.error = "Error fetching data";
    });
};

});

app.controller('FansCtrl', function($scope, $http) {

    $scope.loading = true;
    $scope.length = 0;
  $http.get(url+followers)
  .success(function (response) {
          $scope.length = response.length;
          $scope.fans = response;
       $scope.follow_button = "Follow";
       $scope.loading = false;
      })


  .error(function(response) {
      $scope.loading = false;
          $scope.error = "Error fetching data";
    });


    $scope.reload = function() {
     $scope.length = 0;
    $scope.fans = [];

     $scope.loading = true;
  $http.get(url+followers)
  .success(function (response) {
          $scope.length = response.length;
          $scope.fans = response;

       $scope.loading = false;})
  .error(function(response) {
      $scope.loading = false;
          $scope.error = "Error fetching data";
    });
};

});

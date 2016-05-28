zodiacApp.controller('ZodiacController', Controller);

Controller.$inject = ['$scope', 'ZodiacService'];

function Controller($scope, ZodiacService){
    var zodiac = this;
    zodiac.get_horoscope = select;
    $scope.zodiac = zodiac;

    function select(){
        $scope.zodiac.dataLoading = true;
        $scope.horoscopeResult = '<div class="spinner"><div class="bounce1"></div><div class="bounce2"></div><div class="bounce3"></div></div>';
        ZodiacService.get_horoscope($scope.zodiac).then(function (response){
            if(response.status == 200){
                $scope.horoscopeResult = "<h1>" + response.data.title + "</h1>" + response.data.text;
            }else{
                $scope.horoscopeResult = '<div class="bad">' + response.data + '</div>';
            }
        })
    }
}
zodiacApp.factory('ZodiacService', Service);

function Service($http, baseurl, $filter){
    var service = {};
    service.get_horoscope = get_horoscope;

    return service;

    function get_horoscope(data){
        return $http({
            url: baseurl+'/horoscope/?birthday='+$filter('date')(data['birthday'], 'MM-dd', 'UTC'),
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }).then(
            function successCallBack(response){
                return response
            },
            function errorCallBack(response){
                return response
            }
        );
    }

}

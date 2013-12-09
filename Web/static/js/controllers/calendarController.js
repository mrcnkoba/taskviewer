'use strict';
(function () {
    //CALENDAR CONTROLER
    taskViewer.controller('CalendarController', ['$scope', 'dateTimeService',
        function CalendarController($scope, dts) {
            var actualMonday = dts.getMonday(new Date());
            $scope.hours = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"];
            $scope.days = dts.createWeek(new Date());


            //Actions
            $scope.goToNextWeek = function () {
                actualMonday = new Date(actualMonday.getFullYear(), actualMonday.getMonth(), actualMonday.getDate() + 7);
                $scope.days = dts.createWeek(actualMonday);
            };

            $scope.goToPreviousWeek = function () {
                actualMonday = new Date(actualMonday.getFullYear(), actualMonday.getMonth(), actualMonday.getDate() - 7);
                $scope.days = dts.createWeek(actualMonday);
            };
    }]);
})();
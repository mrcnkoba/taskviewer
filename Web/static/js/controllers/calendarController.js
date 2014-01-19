'use strict';
(function () {
    //CALENDAR CONTROLER
    taskViewer.controller('CalendarController', ['$scope', 'dateTimeService',  'storageService', 'tasksService',
        function CalendarController($scope, dts, storageService, tasksService) {
            var actualMonday = dts.getMonday(new Date());
//            $scope.hours = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"];
            $scope.days = dts.createWeek(new Date());
            $scope.hours = [];
            var tasks = $scope.tasks = storageService.get();
            var weekTasks = Enumerable.From(tasks).Where(function(x){
                var dueDate = new Date(x.validToDate).getDate();
                return (dueDate >= actualMonday.getDate()) && (dueDate < actualMonday.getDate() + 7);
            });
            createHours();

            console.log($scope.hours);
            console.log(weekTasks.ToArray());

            //Handlers
            $scope.$on('handleBroadcast', function() {
                tasks = tasksService.tasks;
                weekTasks = Enumerable.From(tasks).Where(function(x){
                    var dueDate = new Date(x.validToDate).getDate();
                    return (dueDate >= actualMonday.getDate()) && (dueDate < actualMonday.getDate() + 7);
                });
                createHours();
                $scope.$apply();
            });

            //Actions
            $scope.goToNextWeek = function () {
                actualMonday = new Date(actualMonday.getFullYear(), actualMonday.getMonth(), actualMonday.getDate() + 7);
                $scope.days = dts.createWeek(actualMonday);
                createHours();
            };

            $scope.goToPreviousWeek = function () {
                actualMonday = new Date(actualMonday.getFullYear(), actualMonday.getMonth(), actualMonday.getDate() - 7);
                $scope.days = dts.createWeek(actualMonday);
                createHours();
            };

            //helpers
            function createHours(){
                $scope.hours = [];
                 for(var i = 0; i < 24; i++){
                    $scope.hours.push({
                        hour: i,
                        tasks: {
                            monday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate());
                            }).ToArray(),
                            tuesday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate()+1);
                            }).ToArray(),
                            wednsday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate()+2);
                            }).ToArray(),
                            thursday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate()+3);
                            }).ToArray(),
                            friday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate()+4);
                            }).ToArray(),
                            saturday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate()+5);
                            }).ToArray(),
                            sunday: weekTasks.Where(function(x){
                                var dueDate = new Date(x.validToDate);
                                return (dueDate.getHours() == i) && (dueDate.getDate() == actualMonday.getDate()+6);
                            }).ToArray()
                        },
                        tooltip: function(weekDay){
                            var text = "";
                            Enumerable.From(this.tasks[weekDay]).ForEach(function(x){
                                text = text + x.title + "\n";
                            });
                            return text;
                        }
                    });
                }
            };
    }]);
})();

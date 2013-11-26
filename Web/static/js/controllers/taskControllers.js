'use strict';
(function(){
    var taskStatus = {
        new: "active",
        removed: "removed"
    };

    //TASKS CONTROLLER
    taskViewer.controller('TasksController', ['$scope', 'storageService', function TasksController($scope, storageService){
        var tasks = $scope.tasks = storageService.get();
        $scope.selectedIndex = 0; 
        
        $scope.$watch('tasks', function(newVal, oldVal){
            if(newVal !== oldVal){
                storageService.put(tasks);    
            }
        }, true);
        
        $scope.$watch('tasks.task.done', function(newVal, oldVal){
            if(newVal !== true){
                this.status = taskStatus.done;   
            }
        }, true);
        
        $scope.filters={};
        
        //Actions
        $scope.add = function(){
            $scope.tasks.push({
                title: this.newTaskTitle,
                description: "",
                validToDate: new Date(),
                done: false,
                priority: 1,
                status: taskStatus.new
            })
            this.newTaskTitle = '';
        };
        
        $scope.applyFilter = function(filter, $index){
            $scope.filters = filter;
            $scope.selectedIndex = $index;
        }        
    }]);
    
    //CALENDAR CONTROLER
    taskViewer.controller('CalendarController', ['$scope', function CalendarController($scope){      
        $scope.hours = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"];    
        $scope.days = ["18 NOV 2013", "19 NOV 2013", "20 NOV 2013", "21 NOV 2013", "22 NOV 2013", "23 NOV 2013", "24 NOV 2013"];

        //Actions
        $scope.goToNextWeek = function(){
          
        };
        
        //Actions
        $scope.goToPreviousWeek = function(){
          
        };
    }]);
})();
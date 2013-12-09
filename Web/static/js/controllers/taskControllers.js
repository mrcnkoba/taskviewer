'use strict';

(function(){
    var taskStatus = {
        new: "active",
        removed: "removed"
    };
    //TODO: controller
    //var tasksControllers = angular.module('tasksControllers', []);
    
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
                title: $scope.newTaskTitle,
                description: "",
                validToDate: new Date(),
                done: false,
                priority: 1,
                status: taskStatus.new
            })
            $scope.newTaskTitle = '';
        };
        
        $scope.applyFilter = function(filter, $index){
            $scope.filters = filter;
            $scope.selectedIndex = $index;
        }        
    }]);
})();
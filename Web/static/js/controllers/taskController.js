'use strict';
(function () {
    var taskStatus = {
        new: "active",
        removed: "removed"
    };

    //TASKS CONTROLLER
    taskViewer.controller('TasksController', ['$scope', 'storageService', 'tasksService',
        function TasksController($scope, storageService, tasksService) {
            var tasks = $scope.tasks = storageService.get();
            var taskInEditMode;
            $scope.selectedIndex = 0;
            $scope.$watch('tasks', function (newVal, oldVal) {
                if (newVal !== oldVal) {
                    storageService.put(tasks);
                    tasksService.broadcastTasks(tasks);
                }
            }, true);

//            $scope.$watch('tasks.task.done', function (newVal, oldVal) {
//                if (newVal !== true) {
//                    this.status = taskStatus.done;
//                }
//            }, true);
            closeEditModeForAny();
            $scope.filters = {};


            //handlers
            $scope.$on('handleBroadcast', function() {
                $scope.tasks = tasksService.tasks;
            });

            //Actions
            $scope.add = function () {
                var task = {
                    title: this.newTaskTitle,
                    description: "",
                    validToDate: new Date(),
                    done: false,
                    priority: 1,
                    status: taskStatus.new
                }
                $scope.tasks.push(task)
                $scope.toggleEdit(task);
                //storageService.add(task);
                this.newTaskTitle = '';
            };



            $scope.toggleEdit = function (task) {
                if(task.editMode){
                    task.editMode = false;
                }else{
                    closeEditModeForAny();
                    task.editMode = true;
                    taskInEditMode = angular.copy(task);
                }
            }

            $scope.saveTask = function(task){
                $scope.toggleEdit(task);
                //storageService.edit(task);
            };

            $scope.cancelEdit = function(task){
                var index = $scope.tasks.indexOf(task);
                $scope.tasks[index] = taskInEditMode;
                $scope.toggleEdit($scope.tasks[index]);
            };

            $scope.remove = function (task) {
                var index = $scope.tasks.indexOf(task)
                $scope.tasks.splice(index,1);
                storageService.remove(task);
            }

            $scope.applyFilter = function (filter, $index) {
                $scope.filters = filter;
                $scope.selectedIndex = $index;
            }

            //helpers
            function closeEditModeForAny(){
                 Enumerable.From(tasks).Where(function (x) {
                     return x.editMode
                 }).ForEach(function(x){
                    x.editMode = false;
                 });
            }
    }]);
})();

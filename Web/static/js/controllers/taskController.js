'use strict';
(function () {
    var taskStatus = {
        new: "active",
        removed: "removed"
    };

    //TASKS CONTROLLER
    taskViewer.controller('TasksController', ['$scope', 'storageService',
        function TasksController($scope, storageService) {
            var tasks = $scope.tasks = storageService.get();
            $scope.selectedIndex = 0;

            $scope.$watch('tasks', function (newVal, oldVal) {
                if (newVal !== oldVal) {
                    storageService.put(tasks);
                }
            }, true);

            $scope.$watch('tasks.task.done', function (newVal, oldVal) {
                if (newVal !== true) {
                    this.status = taskStatus.done;
                }
            }, true);

            $scope.filters = {};

            //Actions
            $scope.add = function () {
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

            $scope.toggleEdit = function (task) {
                task.editMode = !task.editMode;
                zz
            }

            $scope.remove = function (task) {
                //TODO: remove task         
            }

            $scope.applyFilter = function (filter, $index) {
                $scope.filters = filter;
                $scope.selectedIndex = $index;
            }
    }]);
})();
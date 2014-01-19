'use strict';

taskViewer.factory('tasksService', function($rootScope, storageService) {
    var sharedService = {};
    
    sharedService.tasks = [];

    sharedService.broadcastTasks = function(tasks) {
        this.tasks = tasks;
        $rootScope.$broadcast('handleBroadcast');
    };

    return sharedService;
});

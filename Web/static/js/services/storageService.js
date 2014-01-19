'use strict';

taskViewer.factory('storageService', function () {
	var STORAGE_ID = 'taskviewer-angularsone';

	return {
		get: function () {
			return JSON.parse(localStorage.getItem(STORAGE_ID) || '[]');
		},

		put: function (tasks) {
			localStorage.setItem(STORAGE_ID, JSON.stringify(tasks));
		}
	};
});

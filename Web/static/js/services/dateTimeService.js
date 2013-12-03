'use strict';

taskViewer.factory('dateTimeService', function () {
	return {
        createWeek: function(d){
            var days = [];
            var actualMonday = this.getMonday(d);
            for(var i=0; i<7; i++){
                var day = new Date(actualMonday.getFullYear(),actualMonday.getMonth(), actualMonday.getDate()+i);
                var dateName = day.getDate().toString() + "/" + (day.getMonth()+1).toString() + "/" + day.getFullYear().toString()
                days.push(dateName);
            }
            return days;
        },
        
        getMonday: function(d) {
            d = new Date(d);
            var day = d.getDay(),
                diff = d.getDate() - day + (day == 0 ? -6:1); // adjust when day is sunday
            return new Date(d.setDate(diff));
        }
	};
});

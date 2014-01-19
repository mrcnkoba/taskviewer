var directives = angular.module('directives', []);
directives.directive('showonhoverparent',
   [function() {
      return {
         link : function(scope, element, attrs) {
            element.parent().bind('mouseenter', function() {
                element.fadeIn(200);
            });
            element.parent().bind('mouseleave', function() {
                 element.fadeOut(200);
            });
       }
   };
}]);


directives.directive('shadow', [function() {
    return {
        restrict: 'E',
        scope: {
            ngModel: '@of',
            arrayParent: '=',
            onCommit: '&',
            onRevert: '&'
        },
        link: function(scope, el, att) {
            scope.copy = angular.copy(scope.ngModel);
//            angular.extend(scope, copy);
            scope.commit = function() {
                if(scope.arrayParent){
                    scope.arrayParent[scope.arrayParent.indexOf(scope.ngModel)] = scope[att.of];
                }else{
                    scope.ngModel = scope[att.of];
                }
                scope.onCommit();
            };
            
            scope.revert = function(){
                scope[att.of] = angular.copy(scope.ngModel);
                scope.ngModel = angular.copy(scope.copy);
                if(typeof(scope.onRevert) === "function"){
                    scope.onRevert();
                }
            };
        }
    };
}]);

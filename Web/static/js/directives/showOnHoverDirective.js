var directives = angular.module('directives', []);
directives.directive('showonhoverparent',
   function() {
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
});

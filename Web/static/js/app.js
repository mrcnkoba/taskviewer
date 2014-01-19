"use strict";

var taskViewer = angular.module('taskViewer', ['perfect_scrollbar', 'directives', 'ngQuickDate']);

taskViewer.config(function(ngQuickDateDefaultsProvider) {
  return ngQuickDateDefaultsProvider.set({
    closeButtonHtml: "<i class='icon ion-close'></i>",
    buttonIconHtml: "<i class='icon ion-ios7-calendar-outline'></i>",
    nextLinkHtml: "<i class='icon ion-ios7-arrow-forward'></i>",
    prevLinkHtml: "<i class='icon ion-ios7-arrow-back'></i>",

  });
});

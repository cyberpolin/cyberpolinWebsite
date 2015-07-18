(function(){
	
	var app = angular.module('portfolio', ['ngSanitize']);
	
	app.controller('JobController', ['$http', function($http, $scope){
		
		var store = this;
		store.products = [];
		$http.get('/api/job.json').success(function(data){
			store.products = data;
		});
		this.job = store.products[0];

		this.selectJob = function(setJob){
			this.job = setJob;
			$.vegas('stop');
			$.vegas({src:'/img/portfolio/'+setJob.photo, fade:1000});
		};

	}]);

	

})();
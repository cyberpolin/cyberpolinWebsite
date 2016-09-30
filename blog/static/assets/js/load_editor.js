jQuery(function($) {
				$('#_editor2').ace_wysiwyg({
					toolbar:
					[
						{
							name:'font',
							title:'realmente quieres cambiar la fuente?',
							values:['Arial','Verdana','Comic Sans MS']
						},
						null,
						{
							name:'fontSize',
							title:'Tamaños',
							values:{1 : 'Parrafo' , 2 : 'Size#1 Text' , 3 : 'Size#3 Text' , 4 : 'Size#4 Text' , 5 : 'Size#5 Text'}
						},
						null,
						{name:'bold', title:'Bold'},
						{name:'italic', title:'Italic'},
						{name:'strikethrough', title:'Strike'},
						{name:'underline', title:'Underline'},
						null,
						'insertunorderedlist',
						'insertorderedlist',
						'outdent',
						'indent',
						null,
						{name:'justifyleft'},
						{name:'justifycenter'},
						{name:'justifyright'},
						{name:'justifyfull'},
						null,
						{
							name:'createLink',
							placeholder:'Custom PlaceHolder Text',
							button_class:'btn-purple',
							button_text:'Custom TEXT'
						},
						{name:'unlink'},
						null,
						{
							name:'insertImage',
							placeholder:'Custom PlaceHolder Text',
							button_class:'btn-inverse',
							//choose_file:false,//hide choose file button
							button_text:'Set choose_file:false to hide this',
							button_insert_class:'btn-pink',
							button_insert:'Insert Image'
						},
						null,
						{
							name:'foreColor',
							title:'Custom Colors',
							values:['red','green','blue','navy','orange'],
							/**
								You change colors as well
							*/
						},
						/**null,
						{
							name:'backColor'
						},*/
						null,
						{name:'undo'},
						{name:'redo'},
						null,
						'viewSource'
					],
					//speech_button:false,//hide speech button on chrome

					'wysiwyg': {
						hotKeys : {} //disable hotkeys
					}

				}).prev().addClass('wysiwyg-style2');





			});
function updateMarkdown(markdown){
	$('#flask-pagedown-pagedown').val(markdown);
	$('#flask-pagedown-pagedown').trigger('keyup');
}

$(document).ready(function(){
	namespace = '/test';
	var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
	socket.on('connect', function() {
        socket.emit('my event', {data: 'I\'m connected!'});
    });
	socket.on('current markdown', function(msg) {
        updateMarkdown(msg.data);
    });
	socket.on('markdown modification', function(msg) {
		updateMarkdown(msg.data);
	});

		$('#flask-pagedown-pagedown').bind('input propertychange', function(){
			var data = $('#flask-pagedown-pagedown').val();
			socket.emit('markdown edit', {markdown: data})
		});
});
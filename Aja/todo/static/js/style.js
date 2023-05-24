$(document).ready(function(){

    $('#createButton').click(function(){
    var serializeData = $('#createTaskForm').serialize();
    console.log(serializeData)
    });
});
<script>
  $(function() {
    $('#myform').ajaxForm({
      dataType: 'json',
      beforeSend: function() {
        $('#result').append( "beforeSend...\n" );
      },
      complete: function(data) {
        $('#result')
          .append( "complete...\n" )
          .append( JSON.stringify( data.responseJSON ) + "\n" );
      }
    });
  });
</script>

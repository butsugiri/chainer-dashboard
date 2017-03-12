$(document).ready(function() {
    var datetime = $("#date-time").text()
    $('.result-content').each(function() {
        var yAxis = $(this).attr('id');
        var data = {
            dateTime: datetime,
            yAxis: yAxis
        }
        var self = this;
        $.ajax({
                type: 'POST',
                url: '/plot',
                contentType: 'text/plain',
                data: JSON.stringify(data),
                dataType: 'json'
            })
            .done(function(data) {
                var elem = $("<img>").attr('src', data)
                $(self).find('.thumbnail').first().append(elem)
            })
    })

    $('.result-content').each(function() {
        var yAxis = $(this).attr('id');
        var data = {
            dateTime: datetime,
            yAxis: yAxis
        }
        var self = this;
        $.ajax({
                type: 'POST',
                url: '/details',
                contentType: 'text/plain',
                data: JSON.stringify(data),
                dataType: 'json'
            })
            .done(function(data) {
              console.log(data)
              var table = $("<table></table>").attr('class', 'table').append("<thead></thead>")
              table.find("thead").append('<tr><th>' + 'epoch' + '</th><th>' + yAxis + '</th></tr>')
              table.append("<tbody></tbody>")
              for (i=0; i < data.length; i++) {
                table.find('tbody').append('<tr><td>' + i + '</td><td>' + data[i] + '</td></tr>')
              }
              $(self).find(".log-content").first().append(table)
            })
    })


    // なんかバグる
    // $(".nav-stacked li").first().attr('class', 'active')
    // $(".tab-content div").first().attr('class', 'active')
})

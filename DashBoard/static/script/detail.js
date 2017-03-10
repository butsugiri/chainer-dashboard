var plotGraph = function() {
    var self = this;
    var data = {
        dateTime: $("#date-time").text()
    }
    // console.log(data);
    $.ajax({
            type: 'POST',
            url: '/plot',
            contentType: 'text/plain',
            data: JSON.stringify(data),
            dataType: 'json'
        })
        .done(function(data) {
          console.log(data);
          self.name = data;
        })
}

var app = new Vue({
    el: "#graph",
    data: {
      name: ""
    },
    created: function() {
        this.plotGraph()
    },
    methods: {
        plotGraph: plotGraph
    }
})

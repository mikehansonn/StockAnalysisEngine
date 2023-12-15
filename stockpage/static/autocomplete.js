$(function() {
    function navigateToDetailsPage(selectedName) {
        var link = $("<div>").text(selectedName).addClass("search-return-record");
        $("#searched-item-container").append(link);
    }

    $("#search-input").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/autocomplete",
                dataType: "json",
                data: {
                    term: request.term
                },
                success: function(data) {
                    response(data.results);
                }
            });
        },
        minLength: 1,
        select: function(event, ui) {
            var selectedName = ui.item.value;
            navigateToDetailsPage(selectedName);
        }
    });

    $("#search-input").on("keydown", function(event) {
        if (event.which === 13) {
            var enteredText = $(this).val();
            navigateToDetailsPage(enteredText);
        }
    });
});

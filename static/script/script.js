const fields = ["eq", "xu", "xl", "crit", "x"]
let selected = "Bisection"

$(function() {
    
    updateInputFields()
    $("#selection").val(selected)
    
    $("#calculate").on("click", () => onCalculate())
    $("#clear").on("click", () => {
        fields.forEach(e => {
            const id = "#" + e;
            $(id).val("");
        })
    })
    $("#selection").on("change", () => {
        selected = $("#selection").val()
        updateInputFields()
    })
    
})

function onCalculate() {
    let fields = []
    if (selected == "Non-linear") {
        //TODO: Integrate non-linear
        // fields = ["eq", "xu", "xl", "crit"]
    }else if (selected == "Simple Fix Iteration" || selected == "Newton Rhapson"){
        fields = ["eq", "x", "crit"]
    }else {
        fields = ["eq", "xu", "xl", "crit"]
    }

    let data = new Object()

    fields.forEach(e => {
        const id = "#" + e
        data[e] = $(id).val()
    })
    data["selected"] = selected;
    data = JSON.stringify(data)
    $.post("receiver", data, function(response) {
        const recieved = JSON.parse(response)
        const final = "<label> Root = " + recieved.final + "</label>"
        const selectedLabel = "<label>" + selected + "</label>"
        $("#table-container").children().remove()
        $("#table-container").append(selectedLabel)
        $("#table-container").append(final)
        $("#table-container").append(recieved.table)
        $("#table-container").hide()
        $("#table-container").fadeIn()
    })
}

function updateInputFields() {
    // $("#input-container").children().fadeOut();
    if (selected == "Non-linear") {
        // six inputs
        $(".four-input").hide()
        $(".three-input").hide()
        $(".six-input").show()
    } else if (selected == "Simple Fix Iteration" || selected == "Newton Rhapson") {
        // three inputs
        $(".six-input").hide()
        $(".four-input").hide()
        $(".three-input").show()
    } else {
        // four inputs
        $(".six-input").hide()
        $(".three-input").hide()
        $(".four-input").show()
    }
}
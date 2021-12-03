const fields = ["eq", "xu", "xl", "crit", "x"]
let selected = "Bisection"

$(function() {

    // $("#three-inputs").hide()
    // $("#six-inputs").hide()
    
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
        console.log(response)
        const l = "<label>" + selected + "</label>"
        $("#table-container").children().remove()
        $("#table-container").append(l)
        $("#table-container").append(response)
        $("#table-container").hide()
        $("#table-container").fadeIn()
    })
}

function updateInputFields() {
    // $("#input-container").children().fadeOut();
    if (selected == "Non-linear") {
        // six inputs
    } else if (selected == "Simple Fix Iteration" || selected == "Newton Rhapson") {
        // three inputs
        $(".four-input").hide()
        $(".three-input").show()
    } else {
        $(".three-input").hide()
        // four inputs
        $(".four-input").show()
    }
}
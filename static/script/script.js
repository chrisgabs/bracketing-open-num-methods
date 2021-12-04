const fields = ["eq", "xu", "xl", "crit", "x", "eq1l", "eq1r", "eq2l", "eq2r", "x0", "y0"]
let selected = "Bisection"

$(function() {
    
    updateInputFields()
    $("#selection").val(selected)
    
    $("#calculate").on("click", () => {
        $("#table-container").children().remove()
        $("#table-container").append('<label">' + selected + "</label>")
        $("#loading-container").show()
        onCalculate()
    })
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
    let data = new Object()
    let fields = []

    if (selected == "Non-linear") {
        fields = ["eq1l", "eq1r", "eq2l", "eq2r", "x0", "y0", "crit"]
    }else if (selected == "Simple Fix Iteration" || selected == "Newton Rhapson"){
        fields = ["eq", "x", "crit"]
    }else {
        fields = ["eq", "xu", "xl", "crit"]
    }

    fields.forEach(e => {
        const id = "#" + e
        data[e] = $(id).val()
    })
    data["selected"] = selected;
    data = JSON.stringify(data)
    $.post("receiver", data, (response) => {
        displayResponse(response)
    })
}

function updateInputFields() {
    $("#table-container").children().remove()
    $("#loading-container").hide()
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

function displayResponse(response) {
    console.log(response)
    let received = response;
    try {
        received = JSON.parse(response)
    } catch (err) {
        $("#table-container").append(received)
    }
    const final = "<label>" + received.final + "</label>"
    $("#table-container").append(final)
    $("#table-container").append(received.table)
    $("#table-container").hide()
    $("#table-container").fadeIn()
    if(response != null) {
        $("#loading-container").fadeOut('fast')
    }
}
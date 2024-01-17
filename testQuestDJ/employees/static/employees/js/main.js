$(document).ready(function () {
    // $(document).on("mouseenter", ".employee", function () {
    //     if ($(this).parent().find(".accordion-body").children().length < 1) {
    //         const accordionContainer = $(this).parent().find(".accordion-body")
    //         $.ajax({
    //             url: 'get_employees_by_manager_id',
    //             method: 'post',
    //             dataType: 'json',
    //             data: { id: $(this).data("pk"), page: page_number },
    //             success: function (employees_list) {
    //                 add_employees_in_mamanger(accordionContainer, employees_list)
    //             }
    //         });
    //     }
    // });
})

function hide_sibling(element) {
    if ($(element).hasClass("collapsed")) {
        $(element).closest(".accordion").siblings().removeClass("hidden")
    } else {
        $(element).closest(".accordion").siblings().addClass("hidden")
        const accordionContainer = $(element).closest(".accordion").find(".accordion-body")
        if ($(element).closest(".accordion").find(".accordion-body").children().length < 1) {
            $.ajax({
                url: 'get_employees_by_manager_id',
                method: 'post',
                dataType: 'json',
                data: { id: $(element).closest(".employee").data("pk") },
                success: function (employees_list) {
                    add_employees_in_mamanger(accordionContainer, employees_list)
                }
            });
        }
    }
}

function add_employees_in_mamanger(accordionContainer, employees_list) {
    employees_list.forEach(function (employee) {
        var accordion = $('<div class="accordion accordion">')
        var accordionItem = $('<div class="accordion-item">');
        accordionItem.append('<h2 class="accordion-header employee"  data-pk="' + employee.pk + '">\
            <button  onclick="hide_sibling(this)" class="accordion-button collapsed d-flex gap-4" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne' + employee.pk + '" aria-expanded="false" aria-controls="panelsStayOpen-collapseOne' + employee.pk + '" >\
                <span class="fs-5 fw-medium">Name: ' + employee.fields.full_name + '</span>\
                <span class="fs-5 fw-medium">Position: ' + employee.fields.position + '</span>\
                <span class="fs-5 fw-medium">Acceptance date: ' + employee.fields.acceptance_date + '</span>\
            </button>\
        </h2>');
        accordionItem.append('<div id="panelsStayOpen-collapseOne' + employee.pk + '" class="accordion-collapse collapse">\
            <div class="accordion-body">\
                <!-- Дополнительные данные или содержимое по вашему выбору -->\
            </div>\
        </div>');

        accordion.append(accordionItem)
        accordion.append("</div>")
        accordionContainer.append(accordion);
    });
}
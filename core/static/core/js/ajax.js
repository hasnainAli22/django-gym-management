$(document).ready(function() {
    // Add to cart Button
    $('#add-button').click(function(e){
        e.preventDefault(); // Prevent the default behaviour of the click
        $.ajax({
            type:'POST',
            url: cart_add_url,
            data: {
                product_id : $('#add-button').val(),
                product_quantity: $('#select option:selected').text(),
                csrfmiddlewaretoken: csrf_token,
                action: 'post'
            },
            success: function(data){
                //Handle the ajax response
                $('#cart-qty').text(data.qty)

            },
            error: function(xhr, status, error){
                //Handle the ajax error

            }

        })

    }); // End Add to Cart Button Functionality


    // Delete From Cart Functionality
    $('.delete-button').click(function(e){
        e.preventDefault() // Don't do the default behaviour
        var $button = $(this)
        var product_id = $button.data('index');
        console.log(product_id)
        $.ajax({
            url:cart_delete_url,
            type:'POST',
            data:{
                product_id,
                csrfmiddlewaretoken: csrf_token,
                action:'post'
            },
            success:function(data){
                // After the success response got by the ajax request
                // 1. Update the cart number
                $('#cart-qty').text(data.qty)
                // 2. Update the subtotal
                $('#subtotal').text(data.subtotal)
                // 3. Remove the product card
                $button.closest('.product-item').remove()


            },
            error: function(xhr, status, error){
                // In the case of faliure of the ajax request

            }
        })

    }); // End Delete From Cart functionality

    // Update the Cart
    $('.update-button').click(function(e){
        e.preventDefault()
        var $button = $(this);
        var product_id = $button.data('index');
        var product_quantity = $button.siblings('select').find('option:selected').val()
        // console.log(product_id, product_quantity)

        $.ajax({
            type:'POST',
            url:cart_update_url,
            data:{
                action:'post',
                csrfmiddlewaretoken:csrf_token,
                product_quantity,
                product_id

            },
            success:function(data){
                $('#cart-qty').text(data.qty)
                // 2. Update the subtotal
                $('#subtotal').text(data.subtotal)
                // update the product price
                $button.closest('.product-item').find('.product-price').text(`$ ${data.product_price}`)

            }
        });
    });// End Update the cart
})
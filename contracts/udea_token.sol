//SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

import "OpenZeppelin/openzeppelin-contracts@4.0.0/contracts/token/ERC20/ERC20.sol";


/**
 * @dev Implementation of Udea Token
 * 
 * This token is mean to be used to buy products and services at Universidad de Antioquia.
 *
 * The Udea token is equivalent to 1 colombian peso.
 *
 * The Udea token has no decimals.
 *
 * An adress can get as many Udea as it wants but
 * the systems only supports transactions between 100000 to 1000000 colombian pesos,
 * so it is recommended to avoid accumulating the token on one address and instead
 * you should distribute it among several addresses.
 *
 * You can exchange  wei for Udea.
 *
 * The conversions were taken from https://www.coinbase.com/converter/eth/cop, they are
 * the closest number of wei equivalent to 1 colombian peso and
 * were taken on 30/07/2022.
 *
 * The contract can work with eth but it has to be converted to wei first
*/
contract UdeaToken is ERC20 {

    string private err_outside_limit = "Your amount is outside the limits";
    string private err_not_enough_balance = "You don't have enough balance";

    uint256 private conversion_rate = 130000000000; // wei = 1 colombian peso
    uint256 private min_token_amount = 100000;
    uint256 private max_token_amount = 1000000;
    
    /**
     * @dev Sets the name of the token and its symbol.
     *
    */   
    constructor() ERC20("UdeaToken", "Udea")
    {
    }

    /**
     * @dev Returns the number of decimals used to get its user representation.
     *
     * Overrides {ERC20-decimals}
    */
    function decimals() 
        public
        view
        override
        returns (uint8) 
    {
        return 0;
    }

    /**
     * @dev Returns the amount of wei equivalent to one Udea
     *
    */      
    function getConversionRate()
        public
        view
        returns(uint256)
    {
        return conversion_rate;
    }

    /**
     * @dev Returns the amount of Udea equivalent to the given wei and the reminder,
     * for the wei that could not be converted.
     *
     * Requirements:
     *
     * - `amount` has to be a wei quantity.
     * 
    */   
    function convertWeiToUdea(uint256 amount)
        public
        view
        returns(uint256, uint256)
    {
        return (amount / conversion_rate, amount % conversion_rate);
    }

    /**
     * @dev Returns the amount of wei equivalent to the given Udea.
     *
     * Requirements:
     *
     * - `amount` has to be a Udea quantity.
    */   
    function convertUdeaToWei(uint256 amount)
        public
        view
        returns(uint256)
    {
        return amount * conversion_rate;
    }

    /**
     * @dev Checks if an amount is inside a given range.
     *
    */  
    function amountOnRange(uint256 amount, uint256 min_amount, uint256 max_amount)
        public
        pure
        returns(bool)
    {
        return amount >= min_amount && amount <= max_amount;
    }

    /**
     * @dev Exchanges an amount of  wei for Udea.
     *
     * An account can exchange atmost one million Udea.
     *
     * If the account tries to get more than one million Udea, 
     * the transaction will fail.
     *
     * If the conversion is not exact, the remaining wei will be transfer to the
     * change target.
     *
     * The contract holds the payed wei
    */  
    function exchangeWeiToUdea(address account, address change_target)
        external
        payable
    {
        (uint256 udea_amount, uint256 wei_left) = convertWeiToUdea(msg.value);
        require(amountOnRange(udea_amount, min_token_amount, max_token_amount), err_outside_limit);
        _mint(account, udea_amount);
        if(wei_left > 0){
            address payable beneficiary = payable(address(change_target));
            (bool sent, ) = beneficiary.call{value: wei_left}("");
            require(sent, "Failed to send Ether");
        }
    }

    /**
     * @dev Checks if an account has balance to cover the exchange.
     *
     * Requirements:
     *
     * - `amount` has to be a Udea quantity.
    */
    function hasEnoughBalance(address account, uint256 amount)
        public
        view
        returns(bool)
    {
        return amount <= balanceOf(account);
    }

    /**
     * @dev Exchanges Udea for wei.
     *
     * If the caller tries to exchange more than one million Udea or doesn't have
     * the required balance, then the transaction will fail.
     *
     * The Udea exchanged will be burned.
     *
     * Requirements:
     *
     * - the caller must have a balance of at least `amount`.
     * - `amount` has to be a Udea quantity.
    */  
    function exchangeUdeaToWei(uint256 amount)
        external    
    {
        require(amountOnRange(amount, min_token_amount, max_token_amount), err_outside_limit);
        address account = msg.sender;       
        require(hasEnoughBalance(account, amount), err_not_enough_balance);
        address payable beneficiary = payable(account);
        uint256 wei_exchange = convertUdeaToWei(amount);
        (bool sent, ) = beneficiary.call{value: wei_exchange}("");
        require(sent, "Failed to send Ether");
        _burn(account, amount); 
    }

    /**
     * @dev Transfers Udea to a given address.
     *
     * It overrides {IERC20-transfer}.
     *
     * Requirements:
     *
     * - `to` cannot be the zero address.
     * - `amount` has to be between inside a range.
     * - the caller must have a balance of at least `amount`.
     */
    function transfer(address to, uint256 amount) 
        public
        override
        returns (bool) 
    {
        require(amountOnRange(amount, min_token_amount, max_token_amount), err_outside_limit);
        address owner = _msgSender();
        _transfer(owner, to, amount);
        return true;
    }

}

const Migrations = artifacts.require("government");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};

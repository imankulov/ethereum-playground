compile: user_sol_userRecords.abi user_sol_userRecords.bin
clean:
	rm -f *.abi *.bin

user_sol_userRecords.abi: user.sol
	npx solcjs --abi user.sol

user_sol_userRecords.bin: user.sol
	npx solcjs --bin user.sol


.PHONY: compile clean

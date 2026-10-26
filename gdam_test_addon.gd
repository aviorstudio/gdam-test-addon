@tool
extends EditorPlugin

func _enter_tree() -> void:
	print("gdam Test Addon enabled")

func _exit_tree() -> void:
	print("gdam Test Addon disabled")

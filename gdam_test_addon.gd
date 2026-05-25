@tool
extends EditorPlugin

func _enter_tree() -> void:
	print("GDAM Test Addon enabled")

func _exit_tree() -> void:
	print("GDAM Test Addon disabled")

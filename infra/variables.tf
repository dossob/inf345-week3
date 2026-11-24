variable "image" {
  description = "The published Notes API image pinned to a full commit SHA."
  type        = string
  default     = "ghcr.io/dossob/inf345-week3:afaa7f911bb2002d169f828bf4c48e79a972ddca"
}

variable "internal_port" {
  description = "The port my service listens on inside the container - the contract's PORT"
  type        = number
  default     = 8080
}

variable "host_port" {
  description = "The port on my laptop: http://localhost:<host_port>/healthz"
  type        = number
  default     = 8080
}

variable "restart_policy" {
  description = "What Docker does when my service exits: no, on-failure, always or unless-stopped"
  type        = string
  default     = "no"
}
